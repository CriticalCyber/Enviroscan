// EnviroScan Frontend JavaScript

// DOMContentLoaded event listener
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initializeApp();
    
    // Set up event listeners
    setupEventListeners();
});

// Initialize the application
function initializeApp() {
    console.log('EnviroScan frontend initialized');
    
    // Set current year in footer
    const currentYear = new Date().getFullYear();
    document.querySelectorAll('footer p').forEach(p => {
        if (p.textContent.includes('Data Sources')) return;
        p.innerHTML = p.innerHTML.replace(/\d{4}/g, currentYear);
    });
    
    // Smooth scrolling for navigation links
    setupSmoothScrolling();
}

// Set up event listeners
function setupEventListeners() {
    // Comparison period selector
    const comparisonSelector = document.getElementById('comparison-period');
    if (comparisonSelector) {
        comparisonSelector.addEventListener('change', handleComparisonChange);
    }
    
    // Navigation links
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', handleNavClick);
    });
}

// Set up smooth scrolling for navigation links
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Handle comparison period change
function handleComparisonChange(event) {
    const selectedPeriod = event.target.value;
    console.log(`Comparison period changed to: ${selectedPeriod}`);
    
    // In a real implementation, this would update the visualizations
    // For now, we'll just show a message
    alert(`Would load change detection data for period: ${selectedPeriod}`);
}

// Handle navigation link clicks
function handleNavClick(event) {
    // This is handled by the smooth scrolling, but we can add additional logic here if needed
    console.log(`Navigating to: ${this.getAttribute('href')}`);
}

// Simulate loading data (in a real implementation, this would fetch actual data)
function loadData() {
    // Show loading indicator
    showLoadingIndicator(true);
    
    // Simulate API call delay
    setTimeout(() => {
        // Hide loading indicator
        showLoadingIndicator(false);
        
        // Update UI with loaded data
        updateUIWithSampleData();
    }, 1000);
}

// Show/hide loading indicator
function showLoadingIndicator(show) {
    const loader = document.getElementById('loading-indicator');
    if (loader) {
        loader.style.display = show ? 'block' : 'none';
    }
}

// Update UI with sample data
function updateUIWithSampleData() {
    // This function would update the UI with actual data in a real implementation
    console.log('UI updated with sample data');
}

// Utility function to format dates
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

// Utility function to calculate statistics
function calculateStatistics(data) {
    if (!data || data.length === 0) return {};
    
    const sum = data.reduce((a, b) => a + b, 0);
    const mean = sum / data.length;
    const min = Math.min(...data);
    const max = Math.max(...data);
    
    return {
        sum: sum,
        mean: mean,
        min: min,
        max: max
    };
}

// Export functions for testing (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initializeApp,
        setupEventListeners,
        handleComparisonChange,
        handleNavClick,
        loadData,
        showLoadingIndicator,
        updateUIWithSampleData,
        formatDate,
        calculateStatistics
    };
}