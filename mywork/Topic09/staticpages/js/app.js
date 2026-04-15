const API_URL = "http://localhost:5000/api/books"; // Change to your API endpoint

$(document).ready(function () {
    loadBooks();

    // CREATE
    $("#createBook").click(function () {
        const book = {
            title: $("#title").val(),
            author: $("#author").val()
        };

        $.ajax({
            url: API_URL,
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify(book),
            success: function () {
                $("#title").val("");
                $("#author").val("");
                loadBooks();
            }
        });
    });
});

// READ
function loadBooks() {
    $.ajax({
        url: API_URL,
        method: "GET",
        success: function (books) {
            const tbody = $("#booksTable tbody");
            tbody.empty();

            books.forEach(book => {
                tbody.append(`
                    <tr>
                        <td>${book.id}</td>
                        <td><input type="text" value="${book.title}" id="title-${book.id}"></td>
                        <td><input type="text" value="${book.author}" id="author-${book.id}"></td>
                        <td>
                            <button onclick="updateBook(${book.id})">Update</button>
                            <button onclick="deleteBook(${book.id})">Delete</button>
                        </td>
                    </tr>
                `);
            });
        }
    });
}

// UPDATE
function updateBook(id) {
    const updatedBook = {
        title: $(`#title-${id}`).val(),
        author: $(`#author-${id}`).val()
    };

    $.ajax({
        url: `${API_URL}/${id}`,
        method: "PUT",
        contentType: "application/json",
        data: JSON.stringify(updatedBook),
        success: function () {
            loadBooks();
        }
    });
}

// DELETE
function deleteBook(id) {
    $.ajax({
        url: `${API_URL}/${id}`,
        method: "DELETE",
        success: function () {
            loadBooks();
        }
    });
}
