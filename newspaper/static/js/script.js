function menuActive() {
    const currentLacation = location.href;
    const menuItem = document.querySelectorAll('li a');
    const menuLength = menuItem.length;
    for (let i = 0; i < menuLength; i++) {
        if (menuItem[i].href === currentLacation) {
            menuItem[i].className += ' active'
        }
    }
}
menuActive();
