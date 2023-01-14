let imgs = document.querySelectorAll('.skills-img');

for (let img of imgs) {
    img.onclick = function () {
    if (img.classList.contains('skills-img-active')) {
        img.classList.remove('skills-img-active')
    } else {
        img.classList.add('skills-img-active')
    }
}
}
