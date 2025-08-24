// static/gallery/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    const pantoneCards = document.querySelectorAll('.pantone-card');

    // A curated palette of nice, modern colors.
    const colorPalette = [
        '#FF6B6B', '#4ECDC4', '#45B7D1', '#F7B801', '#5F4B8B',
        '#F08A5D', '#B83B5E', '#6A2C70', '#3498DB', '#2ECC71',
        '#F1C40F', '#E67E22', '#E74C3C', '#9B59B6', '#34495E'
    ];

    pantoneCards.forEach(card => {
        // Pick a random color from the palette
        const randomColor = colorPalette[Math.floor(Math.random() * colorPalette.length)];
        card.style.backgroundColor = randomColor;
    });
});
