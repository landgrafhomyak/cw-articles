function expand(code, elem) {
    elem.parentElement.children[0].onclick = () => {
        collapse(code, elem)
    }
    elem.parentElement.children[1].onclick = () => {
        collapse(code, elem)
    }
    elem.parentElement.nextElementSibling.classList.remove("collapsed")
}

function collapse(code, elem) {
    elem.parentElement.children[0].onclick = () => {
        expand(code, elem)
    }
    elem.parentElement.children[1].onclick = () => {
        expand(code, elem)
    }
    elem.parentElement.nextElementSibling.classList.add("collapsed")
}

function change_lang(code, id, elem) {
    elem.parentElement.children[1].children[0].classList.add("unselected")
    elem.parentElement.children[1].children[1].classList.add("unselected")
    elem.parentElement.children[1].children[2].classList.add("unselected")
    elem.parentElement.children[1].children[id].classList.remove("unselected")
    elem.parentElement.children[2].classList.remove("selected")
    elem.parentElement.children[3].classList.remove("selected")
    elem.parentElement.children[4].classList.remove("selected")
    elem.classList.add("selected")
    elem.parentElement.nextElementSibling.firstElementChild.children[0].classList.add("unselected")
    elem.parentElement.nextElementSibling.firstElementChild.children[1].classList.add("unselected")
    elem.parentElement.nextElementSibling.firstElementChild.children[2].classList.add("unselected")
    elem.parentElement.nextElementSibling.firstElementChild.children[id].classList.remove("unselected")
}