"use strict";


/* ======= Isotope plugin ======= */
/* Ref: http://isotope.metafizzy.co/ */
// init Isotope 

const isotopeContainer = document.querySelector('.isotope');
const filterItems = document.querySelectorAll('#filters .btn');

imagesLoaded(isotopeContainer, function () {
	
	var iso = new Isotope( isotopeContainer, {
	  // options
	  itemSelector: '.item',
	  layoutMode: 'fitRows'
	  
	});
	
	// filter items on click
	filterItems.forEach((filterItem) => {
	
		filterItem.addEventListener('click', (e) => {
			
			console.log('clicked');
			
			let filterValue = filterItem.getAttribute('data-filter');
			
			// arrange - https://isotope.metafizzy.co/methods.html
			iso.arrange({ filter: filterValue });
			
			
			//toggle active class
			for (let siblingFilterItem of filterItem.parentNode.children) {
		        siblingFilterItem.classList.remove('is-checked');
		    }
			filterItem.classList.add('is-checked');

		});

	});
})
