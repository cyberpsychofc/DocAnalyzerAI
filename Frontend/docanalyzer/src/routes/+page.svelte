<script>
    let supported_docs = ['txt','pdf'];
    let listener;
    let github = "https://github.com/cyberpsychofc";
    let backend_url = "http://localhost:8080/upload";

    let clickForm = () => {
        listener.click();
    }
    let handleFileInput = (event) => {
        event.preventDefault();
        const file = listener.files[0];

        if (file) {
            const form = new FormData();
            form.append('file', file);

            const fetchParam = {
                method: 'POST',
                body: form,
            };

            fetch(backend_url, fetchParam)
                .then(() => console.log('File sent to Spring'))
                .catch(error => console.error('Error:', error));
            location.replace("http://localhost:8501");
        } else {
            console.log('No file selected');
        }
    };
</script>

<nav>
    <a href="/" class="nav-bar">Analyse</a>
    <a href="" class="nav-bar">Donate</a>
    <a href={github} class="nav-bar">Github</a>
    <a href="" class="nav-bar">About</a>
</nav>
<div class="container">
    <h1 class="title">
        DocAnalyzer
    </h1>
    <div>
        <p class="sub-title">Upload files you want the AI to analyse and Ask Questions!</p>
        <form id="uploadFile" enctype="multipart/form-data">
            <input type="file" id="uploadInput" on:change={handleFileInput} bind:this={listener} style="display: none">
            <button type="button" class="file_input" on:click={clickForm}>Upload</button>
        </form>

        <p>Supported formats:
        {#each supported_docs as format, i}
            {#if i != supported_docs.length - 1}
                .{format},&nbsp
            {:else}
                .{format}
            {/if}
        {/each}
            and more coming soon</p>
    </div>
</div>
<footer>Copyright © Om Aryan | <a class="footlink" href={github}>cyberpsych</a></footer>

<style>
    .container{
        max-width: 680px;
        margin: 40px auto;
    }
    .title{
        font-size: xxx-large;
        font-family: "Bell MT";
        margin-left: 180px;
        padding: 36px;
        display: inline-block;
        position: relative;
        color: #000000;
    }
    .sub-title{
        font-family: Bahnschrift;
        font-size: x-large;
    }
    .file_input{
        padding: 25px 285px;
        font-size: large;
        color: white;
        background-color: #04AA6D;
        font-weight: bold;
        font-family: Calibri;
        border-radius: 5px;
        border: 2px solid #04AA6D;
        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.20),0 17px 50px 0 rgba(0,0,0,0.1);
    }
    .file_input:hover{
        padding: 25px 285px;
        font-size: large;
        color: #4d4d4d;
        background-color: #04f697;
        font-weight: bold;
        font-family: Calibri;
        border-radius: 5px;
        border: 2px solid #04f697;
    }

    nav{
        position: fixed;
        font-family: Calibri;
        left: 0;
        top: 0;
        width: 100%;
        color: #000000;
        margin-top: 10px;
        padding: 10px;
        font-size: large;
        text-align: center;
    }
    .nav-bar{
        padding: 10px;
        color: #000000;
        font-family: Bahnschrift;
        text-decoration: none;
        margin-left: 25px;
        margin-right: 25px;
    }
    .nav-bar:hover{
        padding: 10px;
        color: #4d4d4d;
        font-family: Bahnschrift;
        text-decoration: none;
        margin-left: 25px;
        margin-right: 25px;
    }
    .footlink{
        color: #000000;
        font-family: Bahnschrift;
        text-decoration: none;
    }
    .footlink:hover{
        color: #4d4d4d;
        font-family: Bahnschrift;
        text-decoration: none;
    }
    .title:after{
        content: '';
        position: absolute;
        width: 100%;
        transform: scaleX(0);
        height: 2px;
        bottom: 0;
        left: 0;
        background-color: #000000;
        transform-origin: bottom right;
        transition: transform 0.25s ease-out;
    }

    .title:hover:after {
        transform: scaleX(1);
        transform-origin: bottom left;
    }
    footer{
        position: fixed;
        font-family: Calibri;
        font-weight: bold;
        left: 0;
        bottom: 0;
        width: 100%;
        color: #000000;
        padding: 10px;
        font-size: small;
        text-align: center;
    }
</style>