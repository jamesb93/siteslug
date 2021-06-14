<script>
	import '../app.css';
</script>

<svelte:head>
    <title>
        ---
    </title>
</svelte:head>

<main class='container'>
    <slot />
</main>

<style>
    .container {
        display: flex;
        flex-direction: column;
        max-width: 80%;
        margin: 0 auto;
        margin-top: 40%;
    }
</style>