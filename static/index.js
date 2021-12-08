const form = document.querySelector("form")
const inp = form.querySelector("input")
const btn = form.querySelector("button")

form.addEventListener("submit", (e) => {
    e.preventDefault()
    
    inp.setAttribute("disabled", "true")
    btn.setAttribute("disabled", "true")

    console.log(JSON.stringify({ url: inp.value }))

    try {
        fetch("http://127.0.0.1:5000/shorten_url", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: inp.value }),
        })
            .then(resp => {
                console.log(resp)
                return resp.json()
            })
            .then(resp => {
                const oldH = form.querySelector("p")
                if (oldH) {
                    oldH.remove()
                }

                const h = document.createElement("p")
                const a = document.createElement("a")
                
                h.innerHTML = "Your link is "
                a.innerHTML = `${resp.url}`

                a.setAttribute("href", resp.url)
                a.setAttribute("target", "_blank")
                h.appendChild(a)

                form.appendChild(h)
            })
    } catch (e) {
        console.log(e)
    } finally {
        inp.removeAttribute("disabled")
        btn.removeAttribute("disabled")
    }
})