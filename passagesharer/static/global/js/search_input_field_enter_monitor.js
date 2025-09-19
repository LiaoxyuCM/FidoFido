document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('input.search_text_field').addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            window.location.href = '/search/' + document.querySelector('input.search_text_field').value;
        };
    });
});