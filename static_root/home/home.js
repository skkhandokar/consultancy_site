// Get the carousel element
const carousel = document.querySelector('#controls-carousel');

// Get the text element
const text = carousel.querySelector('.slide-in-top');

// Add a listener for the carousel's "afterChange" event
carousel.addEventListener('afterChange', () => {
  // Add the "animate" class to the text element
  text.classList.add('animate');
});


// get references to the buttons and sections

