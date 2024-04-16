<template>
    <div class="wrap">
        <h1 class="form_title">Darts Team's Game</h1>
        <table class="table">
            <thead>
                <tr>
                    <th>Throw Number</th>
                    <th>Nikolay's Score</th>
                    <th>Viktorio's Score</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>286</td>
                    <td>301</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import "../assets/style.css"
export default {
    name: 'Game',
}
</script>

<style scoped>
table {
    border-collapse:separate;
    border:solid #615a73 4px;
    border-radius:6px;
}

td, th {
    border-left:solid #615a73 4px;
    border-top:solid #615a73 4px;
    padding: 10px;
}

th {
    border-top: none;
}

td:first-child, th:first-child {
     border-left: none;
}

</style>