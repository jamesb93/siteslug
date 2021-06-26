<script context="module">
	export async function load({ page }) {
        return { 
            props: {
                id: page.params.type
            }
        };
	}
</script>

<script>
    import { interacted } from '$lib/app.js';
    import { fade } from 'svelte/transition';
    export let id;

    let source, audio;

    function startAudio() {
        source.src = `/sounds/${id}.aac`;
        audio.play();
        audio.load();
        audio.play();
    }

    function handleClick() {
        $interacted = true;
        startAudio();
    }
</script>

<div class='container' transition:fade>
    <div>you are channel {id}</div>
    {#if $interacted === false}
        <button id='start-button' on:click={handleClick} transition:fade>
            play
        </button>
    {/if}
    <div id='volume-warning'>Please turn up the volume on your device</div>
</div>

<audio controls bind:this={audio} loop={true}>
    <source type='audio/aac' bind:this={source}>
    <track kind='captions'>
</audio>

<style>
    audio {display: none}
    .container {
        display: flex;
        flex-direction: column;
        font-size: 40px;
        gap: 50px;
    }

    #start-button {
        font-family: var(--font);
        border: 1px solid rgb(230, 230, 230);
        background: none;
        -webkit-appearance: none;
        width: max-content;
        margin: 0 auto;
        padding: 10px;
    }

    #volume-warning {
        font-size: 15px;
        color: grey;
    }
    
</style>
