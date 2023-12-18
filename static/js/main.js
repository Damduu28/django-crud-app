const navbar = document.querySelector('.navbar')
const togglerBar = document.querySelector('.toggler.bar i')
const togglerClose = document.querySelector('.toggler.close i')
const titles = document.querySelectorAll('.title')
const searchForm = document.querySelector('.entrie__search > form')
const searchInput = document.querySelector('input[type="search"]')
const filterBtn = document.querySelector('.filter__btn')
const showEntries = document.querySelector('.show__entries')
const messages = document.querySelector('.messages')
const eyeIcons = document.querySelectorAll('.field__group .fa-eye')
const crudForm = document.querySelector('[data-crud-form]')
const image = document.getElementById('c__img')
const new__img = document.querySelector('.new__img')
const color = document.querySelector('.color')
const crud__checks = document.querySelectorAll('.crud__check')
const tBody = document.querySelector('table tbody')

const showEntryForm = document.querySelector('.entry__form')
const showEntry = document.querySelector('.show__entry')

document.addEventListener('DOMContentLoaded', setRangeValue)

if (navbar != null) {
    togglerBar.addEventListener('click', () => {
        navbar.classList.add('active')
    })
    
    togglerClose.addEventListener('click', () => {
        navbar.classList.remove('active')
    })
}


document.addEventListener('click', e => {
    let isDropdownBtn = e.target.matches('[data-dropdown-btn]')

    if (!isDropdownBtn && e.target.closest('[data-dropdown]') != null) return;

    let currentDropdown
    if (isDropdownBtn) {
        currentDropdown = e.target.closest('[data-dropdown]')
        currentDropdown.classList.toggle('active')
    }

    document.querySelectorAll('[data-dropdown].active').forEach(dropdown => {
        if (dropdown === currentDropdown) return
        dropdown.classList.remove('active')
    });
})

if (searchForm != null) {
    searchForm.addEventListener('submit', e => {
        e.preventDefault()
    })
    
    searchInput.addEventListener('keyup', searchEntry)    
}


function searchEntry() {
    let inputValue = this.value
    inputValue = inputValue.toLowerCase()

    for (let i = 0; i < titles.length; i++) {
        let titleText = titles[i].innerText || titles[i].textContent;
        let titleRow = titles[i].parentElement.parentElement
        titleText = titleText.toLowerCase()
        if (titleText.includes(inputValue)) {
            titleRow.style.display = ""
        } else {
            titleRow.style.display = "none"
        }
    }
}

if (showEntryForm != null) {
    showEntryForm.addEventListener('submit', e => {
        e.preventDefault()
    })
    
    showEntry.addEventListener('change', (e) => {
        showEntryForm.submit()
    })
}


function setRangeValue() {
    let url = window.location.search
    let result = +(url.split('=')[1])
    
    let options = document.querySelectorAll('.show__entry option')
    for (let i = 0; i < options.length; i++) {
        let optionValue = +(options[i].value);
        if (optionValue === result) {
            showEntry.value = result
        }
    }
}

if (filterBtn != null) {
    filterBtn.addEventListener('click', () => {
        showEntries.classList.toggle('active')
    })
}


if (eyeIcons) {
    eyeIcons.forEach(icon => {
        icon.addEventListener('click', e => {
            let passInput = e.target.previousElementSibling
            if (passInput.type === 'password') {
                passInput.type = 'text'
                icon.classList.replace('fa-eye', 'fa-eye-slash')
            } else {
                passInput.type = 'password'
                icon.classList.replace('fa-eye-slash', 'fa-eye')
            }
        })
    });
}

setTimeout(() => {
    if (messages !== null) {
        messages.style.display = "none"
    }
}, 4000);

function randomColor() {
    return Math.floor(Math.random() * 16777215).toString(16)
}

randomColor()


// console.log(image.files)
if (crudForm != null) {
    crudForm.addEventListener('submit', () => {
        color.value = randomColor()
    })
    document.querySelector('.color').value = ""
}


function showImage(event) {
    if (FileReader) {
        var reader = new FileReader();
        reader.readAsDataURL(event.files[0])
        reader.onload = function(e) {
            var img = new Image();
            img.src = e.target.result;
            new__img.src = img.src;
            new__img.classList.add('active')
        }
    }
}

for (let i = 0; i < crud__checks.length; i++) {
    crud__checks[i].addEventListener('change', function() {
        let parentEl = this.parentElement.parentElement
        let crudAction = parentEl.querySelector('.action > div')
        if (this.checked) {
            crudAction.classList.add('active')
            tBody.classList.add('active')
            parentEl.classList.add('active')
        } else {
            crudAction.classList.remove('active')
            tBody.classList.remove('active')
            parentEl.classList.remove('active')
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    let tableBody = document.querySelector('table tbody')
    if (!tableBody.classList.contains('active')) return
    for (let i = 0; i < crud__checks.length; i++) { 
        if (crud__checks[i].checked != true) {
            crud__checks[i].disabled = true
        }
    }
})