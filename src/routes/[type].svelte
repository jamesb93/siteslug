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
    import { onMount } from 'svelte';
    import { interacted } from '$lib/app.js';
    import { fade } from 'svelte/transition';
    export let id;
    let source, audio;
    let ready = false;
    let loaded = false;
    let paused = true;

    onMount(async () => {
        source.src = `/sounds/${id}.mp3`;
        ready = true;
        loaded = true;
        console.log(audio.volume)
    })

    function toggleAudio() {
        if (audio.paused) {
            audio.play();
            audio.load();
            audio.play();
        } else {
            audio.pause();
        }
        paused = audio.paused;
    }

    function handleClick() {
        $interacted = true;
        toggleAudio();
    }
</script>

<div class='container' transition:fade>
    <div>sie sind kanal nr. {id}</div>
    <div>you are channel {id}</div>
    {#if (ready && loaded)}
    <button id='start-button' on:click={handleClick} transition:fade>
        {#if paused}
        play
        {:else}
        stop
        {/if}
    </button>
    {/if}
</div>

<audio controls bind:this={audio} loop={true}>
    <source type='audio/mp3' bind:this={source}>
    <track kind='captions'>
</audio>

<style>
    audio {display: none}

    .container {
        display: flex;
        flex-direction: column;
        font-size: 20px;
        gap: 50px;
    }

    #start-button {
        font-family: var(--font);
        border: 1px solid rgb(230, 230, 230);
        background: none;
        -webkit-appearance: none;
        width: 180px;
        margin: 0 auto;
        padding: 10px;
    }

    #start-button:active {
        background: rgb(238, 238, 238);
    }
</style>
