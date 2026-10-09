/**
 * app.js
 * Plain Vanilla JavaScript for Scripture Chronos (Bible Verse & Chronology Explorer).
 * Zero external libraries or frameworks.
 */

(function () {
  'use strict';

  // --- APPLICATION STATE ---
  const state = {
    currentVerse: null,
    verseHistory: [],       // History stack of viewed verse objects
    historyIndex: -1,       // Current position in the history stack
    metadata: null,
    activeFilters: {
      q: '',
      book: '',
      chapter: '',
      verse: '',
      translation: '',
      era: '',
      time: '',
      testament: ''
    },
    isSearching: false,
    debounceTimer: null
  };

  // --- DOM ELEMENT REFERENCES ---
  const elements = {
    // Theme
    themeToggleBtn: document.getElementById('themeToggleBtn'),

    // Omni Search
    omniSearchInput: document.getElementById('omniSearchInput'),
    clearSearchBtn: document.getElementById('clearSearchBtn'),
    executeSearchBtn: document.getElementById('executeSearchBtn'),

    // Quick Filters & Pills
    testamentPills: document.querySelectorAll('[data-testament]'),
    translationPills: document.querySelectorAll('[data-translation]'),
    toggleAdvancedFiltersBtn: document.getElementById('toggleAdvancedFiltersBtn'),
    advancedFilterDrawer: document.getElementById('advancedFilterDrawer'),

    // Advanced Filter Inputs
    filterBook: document.getElementById('filterBook'),
    filterChapter: document.getElementById('filterChapter'),
    filterVerse: document.getElementById('filterVerse'),
    filterTranslation: document.getElementById('filterTranslation'),
    filterEra: document.getElementById('filterEra'),
    filterTimeQuery: document.getElementById('filterTimeQuery'),
    applyFiltersBtn: document.getElementById('applyFiltersBtn'),
    resetFiltersBtn: document.getElementById('resetFiltersBtn'),

    // Featured Verse Card
    verseDisplayCard: document.getElementById('verseDisplayCard'),
    verseReference: document.getElementById('verseReference'),
    verseTranslation: document.getElementById('verseTranslation'),
    verseTestament: document.getElementById('verseTestament'),
    verseText: document.getElementById('verseText'),
    verseApproxDate: document.getElementById('verseApproxDate'),
    verseEra: document.getElementById('verseEra'),
    verseAuthor: document.getElementById('verseAuthor'),
    verseCategory: document.getElementById('verseCategory'),
    newRandomBtn: document.getElementById('newRandomBtn'),
    copyVerseBtn: document.getElementById('copyVerseBtn'),
    prevVerseBtn: document.getElementById('prevVerseBtn'),
    nextVerseBtn: document.getElementById('nextVerseBtn'),

    // Search Results Section
    resultsBanner: document.getElementById('resultsBanner'),
    resultsCountText: document.getElementById('resultsCountText'),
    viewFeaturedBtn: document.getElementById('viewFeaturedBtn'),
    searchResultsSection: document.getElementById('searchResultsSection'),
    resultsList: document.getElementById('resultsList'),
    emptyResultsMessage: document.getElementById('emptyResultsMessage'),
    resetFromEmptyBtn: document.getElementById('resetFromEmptyBtn'),

    // Toast
    toastNotification: document.getElementById('toastNotification'),
    toastMessage: document.getElementById('toastMessage')
  };

  // --- INITIALIZATION ---
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    loadMetadata();
    fetchRandomVerse();
    setupEventListeners();
  });

  // --- THEME MANAGEMENT ---
  function initTheme() {
    const savedTheme = localStorage.getItem('scripture_theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
  }

  function toggleTheme() {
    const currentTheme = document.body.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', newTheme);
    localStorage.setItem('scripture_theme', newTheme);
    updateThemeIcon(newTheme);
  }

  function updateThemeIcon(theme) {
    const iconSpan = elements.themeToggleBtn.querySelector('.theme-icon');
    if (iconSpan) {
      iconSpan.textContent = theme === 'dark' ? '☀️' : '🌙';
    }
  }

  // --- METADATA & DROPDOWNS ---
  async function loadMetadata() {
    try {
      const response = await fetch('/api/metadata');
      const data = await response.json();
      if (data.status === 'success') {
        state.metadata = data.metadata;
        populateDropdowns(data.metadata);
      }
    } catch (err) {
      console.error('Failed to load metadata:', err);
    }
  }

  function populateDropdowns(metadata) {
    // Populate Books with optgroups for Old & New Testament
    const otGroup = document.createElement('optgroup');
    otGroup.label = 'Old Testament (39 Books)';
    const ntGroup = document.createElement('optgroup');
    ntGroup.label = 'New Testament (27 Books)';

    metadata.books.forEach(b => {
      const opt = document.createElement('option');
      opt.value = b.name;
      opt.textContent = `${b.name} (${b.approx_date_written})`;
      if (b.testament === 'Old Testament') {
        otGroup.appendChild(opt);
      } else {
        ntGroup.appendChild(opt);
      }
    });

    elements.filterBook.appendChild(otGroup);
    elements.filterBook.appendChild(ntGroup);

    // Populate Eras
    metadata.eras.forEach(era => {
      const opt = document.createElement('option');
      opt.value = era;
      opt.textContent = era;
      elements.filterEra.appendChild(opt);
    });
  }

  // --- RANDOM VERSE LOGIC ---
  async function fetchRandomVerse() {
    elements.verseDisplayCard.classList.remove('fade-in');
    void elements.verseDisplayCard.offsetWidth; // Trigger reflow

    const params = new URLSearchParams();
    if (state.activeFilters.translation) params.append('translation', state.activeFilters.translation);
    if (state.activeFilters.testament) params.append('testament', state.activeFilters.testament);
    if (state.activeFilters.book) params.append('book', state.activeFilters.book);
    if (state.activeFilters.era) params.append('era', state.activeFilters.era);

    const url = `/api/random${params.toString() ? '?' + params.toString() : ''}`;

    try {
      const response = await fetch(url);
      const data = await response.json();

      if (data.status === 'success' && data.verse) {
        renderFeaturedVerse(data.verse);
      } else {
        showToast(data.message || 'No random verse matched the active filter.');
      }
    } catch (err) {
      console.error('Error fetching random verse:', err);
      showToast('Could not load random verse. Please try again.');
    }
  }

  function renderFeaturedVerse(verse, addToHistory = true) {
    state.currentVerse = verse;

    if (addToHistory) {
      // If user had browsed backward in history and views a new verse, truncate forward history
      if (state.historyIndex < state.verseHistory.length - 1) {
        state.verseHistory = state.verseHistory.slice(0, state.historyIndex + 1);
      }

      // Avoid adding duplicate if identical to currently viewed verse in history
      const currentInHistory = state.verseHistory[state.historyIndex];
      if (!currentInHistory || currentInHistory.id !== verse.id || currentInHistory.translation !== verse.translation) {
        state.verseHistory.push(verse);
        state.historyIndex = state.verseHistory.length - 1;
      }
    }

    // Badges & Reference
    elements.verseReference.textContent = `📖 ${verse.reference}`;
    elements.verseTranslation.textContent = verse.translation_name || verse.translation;
    elements.verseTestament.textContent = verse.testament;

    // Scripture Body
    elements.verseText.textContent = `"${verse.text}"`;

    // Chronology Details
    elements.verseApproxDate.textContent = verse.approx_date_written;
    elements.verseEra.textContent = verse.era;
    elements.verseAuthor.textContent = verse.author || 'Biblical Author';
    elements.verseCategory.textContent = verse.category;

    // Update history navigation button states (enabled vs. greyed-out)
    updateHistoryButtons();

    elements.verseDisplayCard.classList.add('fade-in');
  }

  function updateHistoryButtons() {
    const hasPrev = state.historyIndex > 0;
    const hasNext = state.historyIndex >= 0 && state.historyIndex < state.verseHistory.length - 1;

    elements.prevVerseBtn.disabled = !hasPrev;
    elements.nextVerseBtn.disabled = !hasNext;

    if (hasPrev) {
      const prevVerse = state.verseHistory[state.historyIndex - 1];
      elements.prevVerseBtn.title = `Previous verse in history (${prevVerse.reference})`;
    } else {
      elements.prevVerseBtn.title = 'No previous verse in history';
    }

    if (hasNext) {
      const nextVerse = state.verseHistory[state.historyIndex + 1];
      elements.nextVerseBtn.title = `Next verse in history (${nextVerse.reference})`;
    } else {
      elements.nextVerseBtn.title = 'No next verse in history';
    }
  }

  function showPreviousVerse() {
    if (state.historyIndex > 0) {
      elements.verseDisplayCard.classList.remove('fade-in');
      void elements.verseDisplayCard.offsetWidth; // Trigger reflow for animation
      state.historyIndex--;
      const prevVerse = state.verseHistory[state.historyIndex];
      renderFeaturedVerse(prevVerse, false);
    }
  }

  function showNextVerse() {
    if (state.historyIndex >= 0 && state.historyIndex < state.verseHistory.length - 1) {
      elements.verseDisplayCard.classList.remove('fade-in');
      void elements.verseDisplayCard.offsetWidth; // Trigger reflow for animation
      state.historyIndex++;
      const nextVerse = state.verseHistory[state.historyIndex];
      renderFeaturedVerse(nextVerse, false);
    }
  }

  // --- SPECIFIC VERSE BY ID ---
  async function fetchVerseById(verseId) {
    try {
      const response = await fetch(`/api/verse/${verseId}`);
      const data = await response.json();
      if (data.status === 'success') {
        renderFeaturedVerse(data.verse);
        scrollToFeatured();
      }
    } catch (err) {
      console.error('Failed to fetch verse by id:', err);
    }
  }

  // --- SEARCH LOGIC ---
  async function executeSearch() {
    const q = elements.omniSearchInput.value.trim();
    state.activeFilters.q = q;

    // Collect advanced filter values
    state.activeFilters.book = elements.filterBook.value;
    state.activeFilters.chapter = elements.filterChapter.value.trim();
    state.activeFilters.verse = elements.filterVerse.value.trim();
    state.activeFilters.translation = elements.filterTranslation.value;
    state.activeFilters.era = elements.filterEra.value;
    state.activeFilters.time = elements.filterTimeQuery.value.trim();

    const hasAnyQuery = q || 
      state.activeFilters.book || 
      state.activeFilters.chapter || 
      state.activeFilters.verse || 
      state.activeFilters.translation || 
      state.activeFilters.era || 
      state.activeFilters.time ||
      state.activeFilters.testament;

    if (!hasAnyQuery) {
      hideSearchResults();
      return;
    }

    const params = new URLSearchParams();
    if (state.activeFilters.q) params.append('q', state.activeFilters.q);
    if (state.activeFilters.book) params.append('book', state.activeFilters.book);
    if (state.activeFilters.chapter) params.append('chapter', state.activeFilters.chapter);
    if (state.activeFilters.verse) params.append('verse', state.activeFilters.verse);
    if (state.activeFilters.translation) params.append('translation', state.activeFilters.translation);
    if (state.activeFilters.era) params.append('era', state.activeFilters.era);
    if (state.activeFilters.time) params.append('time', state.activeFilters.time);
    if (state.activeFilters.testament) params.append('testament', state.activeFilters.testament);

    try {
      const response = await fetch(`/api/search?${params.toString()}`);
      const data = await response.json();

      if (data.status === 'success') {
        renderSearchResults(data);
      }
    } catch (err) {
      console.error('Search error:', err);
      showToast('Error performing search. Please check your connection.');
    }
  }

  function renderSearchResults(data) {
    state.isSearching = true;
    elements.resultsBanner.classList.remove('hidden');
    elements.searchResultsSection.classList.remove('hidden');

    const total = data.total;
    elements.resultsCountText.textContent = `Found ${total} verse${total === 1 ? '' : 's'} matching your search`;

    elements.resultsList.innerHTML = '';

    if (total === 0) {
      elements.emptyResultsMessage.classList.remove('hidden');
      return;
    }

    elements.emptyResultsMessage.classList.add('hidden');

    data.verses.forEach(v => {
      const card = document.createElement('div');
      card.className = 'result-card';
      card.innerHTML = `
        <div class="result-card-header">
          <span class="result-ref">📖 ${escapeHtml(v.reference)}</span>
          <span class="badge badge-translation">${escapeHtml(v.translation)}</span>
        </div>
        <p class="result-text">"${escapeHtml(v.text)}"</p>
        <div class="result-meta-row">
          <span class="meta-chip date-chip">⏳ ${escapeHtml(v.approx_date_written)}</span>
          <span class="meta-chip">🏛️ ${escapeHtml(v.era)}</span>
          <span class="meta-chip">🏷️ ${escapeHtml(v.testament)}</span>
          ${v.author ? `<span class="meta-chip">✍️ ${escapeHtml(v.author)}</span>` : ''}
        </div>
      `;

      card.addEventListener('click', () => {
        renderFeaturedVerse(v);
        scrollToFeatured();
      });

      elements.resultsList.appendChild(card);
    });

    // Auto-scroll slightly to show results
    elements.resultsBanner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function hideSearchResults() {
    state.isSearching = false;
    elements.resultsBanner.classList.add('hidden');
    elements.searchResultsSection.classList.add('hidden');
    elements.resultsList.innerHTML = '';
  }

  function scrollToFeatured() {
    elements.verseDisplayCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // --- COPY TO CLIPBOARD ---
  function copyCurrentVerse() {
    if (!state.currentVerse) return;

    const v = state.currentVerse;
    const formatted = `"${v.text}"\n— ${v.reference} [${v.translation_name || v.translation}]\nHistorical Context: Written ${v.approx_date_written} (${v.era})`;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(formatted).then(() => {
        showToast('Verse & historical context copied to clipboard!');
      }).catch(() => {
        fallbackCopyText(formatted);
      });
    } else {
      fallbackCopyText(formatted);
    }
  }

  function fallbackCopyText(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand('copy');
      showToast('Verse & historical context copied to clipboard!');
    } catch (err) {
      showToast('Failed to copy verse.');
    }
    document.body.removeChild(textArea);
  }

  // --- TOAST NOTIFICATION ---
  let toastTimeout = null;
  function showToast(message) {
    if (toastTimeout) clearTimeout(toastTimeout);
    elements.toastMessage.textContent = message;
    elements.toastNotification.classList.remove('hidden');

    toastTimeout = setTimeout(() => {
      elements.toastNotification.classList.add('hidden');
    }, 2800);
  }

  // --- RESET FILTERS ---
  function resetAllFilters() {
    elements.omniSearchInput.value = '';
    elements.clearSearchBtn.classList.add('hidden');

    elements.filterBook.value = '';
    elements.filterChapter.value = '';
    elements.filterVerse.value = '';
    elements.filterTranslation.value = '';
    elements.filterEra.value = '';
    elements.filterTimeQuery.value = '';

    state.activeFilters = {
      q: '',
      book: '',
      chapter: '',
      verse: '',
      translation: '',
      era: '',
      time: '',
      testament: ''
    };

    // Reset pills
    elements.testamentPills.forEach(p => p.classList.toggle('active', p.getAttribute('data-testament') === ''));
    elements.translationPills.forEach(p => p.classList.toggle('active', p.getAttribute('data-translation') === ''));

    hideSearchResults();
    fetchRandomVerse();
  }

  // --- EVENT LISTENERS ---
  function setupEventListeners() {
    // Theme toggle
    elements.themeToggleBtn.addEventListener('click', toggleTheme);

    // Random verse button
    elements.newRandomBtn.addEventListener('click', () => {
      fetchRandomVerse();
    });

    // Copy verse button
    elements.copyVerseBtn.addEventListener('click', copyCurrentVerse);

    // Prev / Next Verse Navigation through viewed history
    elements.prevVerseBtn.addEventListener('click', showPreviousVerse);
    elements.nextVerseBtn.addEventListener('click', showNextVerse);

    // Omni-Search Input Events
    elements.omniSearchInput.addEventListener('input', (e) => {
      const val = e.target.value;
      elements.clearSearchBtn.classList.toggle('hidden', val.length === 0);

      clearTimeout(state.debounceTimer);
      state.debounceTimer = setTimeout(() => {
        if (val.trim().length >= 2) {
          executeSearch();
        } else if (val.trim().length === 0) {
          hideSearchResults();
        }
      }, 350);
    });

    elements.omniSearchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        clearTimeout(state.debounceTimer);
        executeSearch();
      }
    });

    elements.executeSearchBtn.addEventListener('click', () => {
      clearTimeout(state.debounceTimer);
      executeSearch();
    });

    elements.clearSearchBtn.addEventListener('click', () => {
      elements.omniSearchInput.value = '';
      elements.clearSearchBtn.classList.add('hidden');
      hideSearchResults();
      elements.omniSearchInput.focus();
    });

    // Advanced Filters Toggle Drawer
    elements.toggleAdvancedFiltersBtn.addEventListener('click', () => {
      const isHidden = elements.advancedFilterDrawer.classList.contains('hidden');
      elements.advancedFilterDrawer.classList.toggle('hidden', !isHidden);
      elements.toggleAdvancedFiltersBtn.classList.toggle('open', isHidden);
    });

    elements.applyFiltersBtn.addEventListener('click', () => {
      executeSearch();
    });

    elements.resetFiltersBtn.addEventListener('click', resetAllFilters);
    elements.resetFromEmptyBtn.addEventListener('click', resetAllFilters);
    elements.viewFeaturedBtn.addEventListener('click', hideSearchResults);

    // Quick Filter Pills (Testament)
    elements.testamentPills.forEach(pill => {
      pill.addEventListener('click', () => {
        elements.testamentPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state.activeFilters.testament = pill.getAttribute('data-testament');

        if (state.isSearching || elements.omniSearchInput.value.trim()) {
          executeSearch();
        } else {
          fetchRandomVerse();
        }
      });
    });

    // Quick Filter Pills (Translation)
    elements.translationPills.forEach(pill => {
      pill.addEventListener('click', () => {
        elements.translationPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const trans = pill.getAttribute('data-translation');
        state.activeFilters.translation = trans;
        elements.filterTranslation.value = trans;

        if (state.isSearching || elements.omniSearchInput.value.trim()) {
          executeSearch();
        } else {
          fetchRandomVerse();
        }
      });
    });

    // Global Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
      const activeTag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      const isInput = activeTag === 'input' || activeTag === 'select' || activeTag === 'textarea';

      // 'Space' triggers random verse when not focused in input
      if (e.code === 'Space' && !isInput) {
        e.preventDefault();
        fetchRandomVerse();
      }

      // 'ArrowLeft' navigates to previous verse in history
      if (e.key === 'ArrowLeft' && !isInput && !e.altKey && !e.ctrlKey && !e.metaKey) {
        if (state.historyIndex > 0) {
          e.preventDefault();
          showPreviousVerse();
        }
      }

      // 'ArrowRight' navigates to next verse in history
      if (e.key === 'ArrowRight' && !isInput && !e.altKey && !e.ctrlKey && !e.metaKey) {
        if (state.historyIndex >= 0 && state.historyIndex < state.verseHistory.length - 1) {
          e.preventDefault();
          showNextVerse();
        }
      }

      // '/' focuses omni-search
      if (e.key === '/' && !isInput) {
        e.preventDefault();
        elements.omniSearchInput.focus();
        elements.omniSearchInput.select();
      }

      // 'Escape' clears search
      if (e.key === 'Escape') {
        if (state.isSearching) {
          hideSearchResults();
        }
        elements.omniSearchInput.blur();
      }
    });
  }

  // --- HTML ESCAPE HELPER ---
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
})();
