window.onload = () => {
    const eyeButton = document.getElementById('eye-button')
    eyeButton.addEventListener('click', switchValueVisualization)
}

function switchValueVisualization() {
    const viewingValue = document.getElementById('view-value')
    const hidingValue = document.getElementById('hide-value')
    const openedEye = document.getElementById('opened-eye')
    const closedEye = document.getElementById('closed-eye')

    const ishowingValue = hidingValue.classList.contains('inactive-view')
    if (ishowingValue) {
        hideElement(viewingValue)
        hideElement(openedEye)
        showElement(hidingValue)
        showElement(closedEye)
    } else {
        hideElement(hidingValue)
        hideElement(closedEye)
        showElement(viewingValue)
        showElement(openedEye)
    }
}

function hideElement(element){
    element.classList.add('inactive-view')
}

function showElement(element) {
    element.classList.remove('inactive-view')
}