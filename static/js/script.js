/* jshint esversion: 6 */

document.addEventListener('DOMContentLoaded', (event) => {
    const dateField = document.querySelector('#id_requested_date');
    const today = new Date();
    const dd = String(today.getDate()).padStart(2, '0');
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const yyyy = today.getFullYear();

    dateField.min = yyyy + '-' + mm + '-' + dd;
});
