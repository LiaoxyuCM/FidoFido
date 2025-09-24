document.addEventListener('DOMContentLoaded', () => {
    const colorModeToggle = document.cookie.split('; ').find(row => row.startsWith('color_mode='));
    const body = document.body;
    console.log(colorModeToggle);
    if (colorModeToggle === 'color_mode=dark') {
        body.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
    };
    const colormodeLink = document.querySelector('.colormode_link');
    const newMode = body.classList.contains('dark-mode') ? 'light' : 'dark';
    console.log(window.location.pathname);
    colormodeLink.setAttribute('href', `/change_color_mode/${newMode}/?next=${escape(window.location.pathname+window.location.search)}`);
    const img = document.querySelector('.change_colormode_button img');
    if (body.classList.contains('dark-mode')) {
        img.style.filter = 'invert(1)';
        img.setAttribute('src', '/static/global/icon/sunny-outline.svg');
        img.setAttribute('alt', 'Light');
    } else {
        img.setAttribute('src', '/static/global/icon/moon-outline.svg');
        img.setAttribute('alt', 'Dark');
    };
});
