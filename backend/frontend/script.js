document.getElementById("registerForm").addEventListener("submit", function (e) {
    e.preventDefault();  // stop page refresh

    const data = {
        name: document.getElementById("name").value,
        age: document.getElementById("age").value,
        work: document.getElementById("work").value,
        phone: document.getElementById("phone").value
    };

    fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        alert(response.message);
    })
    .catch(err => {
        console.error("Error:", err);
        alert("Something went wrong!");
    });
});

function loadData() {
    fetch("http://127.0.0.1:5000/males")
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById("maleTable");

            table.innerHTML = `
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Work</th>
                    <th>Phone</th>
                </tr>
            `;

            data.forEach(item => {
                table.innerHTML += `
                    <tr>
                        <td>${item.id}</td>
                        <td>${item.name}</td>
                        <td>${item.age}</td>
                        <td>${item.work}</td>
                        <td>${item.phone}</td>
                    </tr>
                `;
            });
        });
}