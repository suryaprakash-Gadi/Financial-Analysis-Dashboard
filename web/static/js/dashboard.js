document.addEventListener('DOMContentLoaded', function() {
    // Animate progress bars
    setTimeout(function() {
        document.querySelectorAll('.progress-bar').forEach(function(bar) {
            const currentWidth = bar.style.width;
            bar.style.width = '0';
            setTimeout(function() {
                bar.style.transition = 'width 1s ease';
                bar.style.width = currentWidth;
            }, 100);
        });
    }, 300);
    
    // Search functionality
    const searchInput = document.getElementById('company-search');
    const clearButton = document.getElementById('clear-search');
    const companySections = document.querySelectorAll('.company-section');
    const noResultsMessage = document.getElementById('no-results');
    
    // Function to handle search
    function handleSearch() {
        const searchTerm = searchInput.value.toLowerCase().trim();
        let resultsFound = false;
        
        // If search term is empty, show all companies
        if (searchTerm === '') {
            companySections.forEach(section => {
                section.style.display = 'flex';
            });
            noResultsMessage.style.display = 'none';
            return;
        }
        
        // Loop through all company sections
        companySections.forEach(section => {
            const companyName = section.getAttribute('data-company');
            const metricElement = section.querySelector('[data-metric]');
            const periodElements = section.querySelectorAll('[data-period]');
            
            // Check if section matches search criteria
            let sectionMatches = companyName && companyName.includes(searchTerm);
            
            // Check metrics
            if (metricElement) {
                const metricTypes = metricElement.getAttribute('data-metric');
                if (metricTypes && metricTypes.includes(searchTerm)) {
                    sectionMatches = true;
                }
            }
            
            // Check periods
            periodElements.forEach(element => {
                const period = element.getAttribute('data-period');
                if (period && period.includes(searchTerm)) {
                    sectionMatches = true;
                }
            });
            
            // Show/hide section based on match
            if (sectionMatches) {
                section.style.display = 'flex';
                resultsFound = true;
            } else {
                section.style.display = 'none';
            }
        });
        
        // Show/hide no results message
        noResultsMessage.style.display = resultsFound ? 'none' : 'block';
    }
    
    // Event listeners
    searchInput.addEventListener('input', handleSearch);
    
    clearButton.addEventListener('click', function() {
        searchInput.value = '';
        handleSearch();
        searchInput.focus();
    });
    
    // Handle Enter key press
    searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            handleSearch();
        }
    });
});