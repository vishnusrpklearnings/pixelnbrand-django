// ============================================
// FORM SPECIFIC JAVASCRIPT
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ========== PHONE NUMBER FORMATTING ==========
    const phoneInput = document.getElementById('phone');
    
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            
            // Format as (XXX) XXX-XXXX
            if (value.length > 0) {
                value = '(' + value.substring(0, 3);
            }
            if (value.length > 4) {
                value = value.substring(0, 4) + ') ' + value.substring(4, 7);
            }
            if (value.length > 9) {
                value = value.substring(0, 9) + '-' + value.substring(9, 13);
            }
            
            e.target.value = value;
        });
    }
    
    // ========== CHARACTER COUNTER FOR TEXTAREA ==========
    const messageTextarea = document.getElementById('message');
    
    if (messageTextarea) {
        // Create character counter
        const counterDiv = document.createElement('div');
        counterDiv.className = 'char-counter';
        counterDiv.style.textAlign = 'right';
        counterDiv.style.fontSize = '0.8rem';
        counterDiv.style.color = '#666';
        counterDiv.style.marginTop = '5px';
        
        messageTextarea.parentNode.appendChild(counterDiv);
        
        function updateCounter() {
            const maxLength = messageTextarea.getAttribute('maxlength') || 1000;
            const currentLength = messageTextarea.value.length;
            counterDiv.textContent = `${currentLength}/${maxLength} characters`;
            
            // Change color if接近limit
            if (currentLength > maxLength * 0.9) {
                counterDiv.style.color = '#ff6b35';
            } else {
                counterDiv.style.color = '#666';
            }
        }
        
        // Initial update
        updateCounter();
        
        // Update on input
        messageTextarea.addEventListener('input', updateCounter);
    }
    
    // ========== FORM SPAM PROTECTION ==========
    const forms = document.querySelectorAll('form:not([data-no-honeypot])');
    
    forms.forEach(form => {
        // Create honeypot field
        const honeypot = document.createElement('input');
        honeypot.type = 'text';
        honeypot.name = 'website';
        honeypot.style.display = 'none';
        honeypot.autocomplete = 'off';
        honeypot.tabIndex = -1;
        
        form.appendChild(honeypot);
        
        // Add timestamp
        const timestamp = document.createElement('input');
        timestamp.type = 'hidden';
        timestamp.name = 'timestamp';
        timestamp.value = Date.now();
        
        form.appendChild(timestamp);
        
        // Form submission validation
        form.addEventListener('submit', function(e) {
            // Check honeypot
            if (honeypot.value !== '') {
                e.preventDefault();
                alert('Spam detected!');
                return false;
            }
            
            // Check timestamp (prevent too fast submissions)
            const submitTime = Date.now();
            const formTime = parseInt(timestamp.value);
            const timeDiff = submitTime - formTime;
            
            if (timeDiff < 2000) { // Less than 2 seconds
                e.preventDefault();
                alert('Please wait a moment before submitting again.');
                return false;
            }
        });
    });
    
    // ========== FORM PERSISTENCE (Optional) ==========
    // Uncomment if you want to save form data locally
    
    /*
    const formFields = document.querySelectorAll('.contact-form input, .contact-form textarea');
    
    // Load saved data
    formFields.forEach(field => {
        const savedValue = localStorage.getItem(`form_${field.name}`);
        if (savedValue) {
            field.value = savedValue;
        }
    });
    
    // Save data on input
    formFields.forEach(field => {
        field.addEventListener('input', function() {
            localStorage.setItem(`form_${this.name}`, this.value);
        });
    });
    
    // Clear on successful submission
    document.querySelector('.contact-form').addEventListener('submit', function() {
        formFields.forEach(field => {
            localStorage.removeItem(`form_${field.name}`);
        });
    });
    */
    
    // ========== FILE UPLOAD PREVIEW ==========
    const fileInput = document.querySelector('input[type="file"]');
    
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                // Check file size (max 5MB)
                const maxSize = 5 * 1024 * 1024; // 5MB in bytes
                if (file.size > maxSize) {
                    alert('File size must be less than 5MB');
                    e.target.value = ''; // Clear the input
                    return;
                }
                
                // Check file type
                const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'];
                if (!allowedTypes.includes(file.type)) {
                    alert('Only JPEG, PNG, GIF images and PDF files are allowed');
                    e.target.value = '';
                    return;
                }
                
                // Preview image if it's an image
                if (file.type.startsWith('image/')) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        // Create preview
                        const previewDiv = document.createElement('div');
                        previewDiv.className = 'file-preview';
                        previewDiv.innerHTML = `
                            <img src="${e.target.result}" style="max-width: 200px; margin-top: 10px;">
                            <button type="button" class="remove-file" style="margin-left: 10px;">Remove</button>
                        `;
                        
                        // Insert after file input
                        fileInput.parentNode.appendChild(previewDiv);
                        
                        // Remove button functionality
                        previewDiv.querySelector('.remove-file').addEventListener('click', function() {
                            previewDiv.remove();
                            fileInput.value = '';
                        });
                    };
                    reader.readAsDataURL(file);
                }
            }
        });
    }
    
});