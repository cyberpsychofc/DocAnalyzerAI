<script>
    let supported_docs = ['txt','pdf'];
</script>
<div class="container">
    <h1 class="title">
        DocAnalyzer
    </h1>
    <div>
        <p class="sub-title">Upload files you want the AI to analyse and Ask Questions!</p>
        <button class="file_input">Upload</button>
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
<footer>Copyright © Om Aryan | cyberpsych</footer>

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
        padding: 20px 200px;
        font-size: large;
        color: white;
        background-color: #04AA6D;
        font-weight: bold;
        font-family: Calibri;
        border-radius: 5px;
        border: 2px solid #04AA6D;
    }
    .file_input:hover{
        padding: 20px 200px;
        font-size: large;
        color: #4d4d4d;
        background-color: #04f697;
        font-weight: bold;
        font-family: Calibri;
        border-radius: 5px;
        border: 2px solid #04f697;
    }

    .title:after {
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
        left: 0;
        bottom: 0;
        width: 100%;
        color: #000000;
        padding: 10px;
        font-size: small;
        text-align: center;
    }
</style>