document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    const uploadProgressBar = document.getElementById('upload-progress-bar');
    const processingProgressBar = document.getElementById('processing-progress-bar');
    const resultDiv = document.getElementById('result');
    const videoContainer = document.getElementById('video-container');
    const videoPlayer = document.getElementById('video-player');
    const downloadLink = document.getElementById('download-link');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const xhr = new XMLHttpRequest();

        xhr.upload.addEventListener('progress', function(e) {
            if (e.lengthComputable) {
                const percentComplete = (e.loaded / e.total) * 100;
                uploadProgressBar.style.width = percentComplete + '%';
                uploadProgressBar.setAttribute('aria-valuenow', percentComplete);
                uploadProgressBar.textContent = Math.round(percentComplete) + '%';
            }
        });

        xhr.addEventListener('load', function() {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                // Simulação de processamento de vídeo
                let processingPercent = 0;
                const processingInterval = setInterval(function() {
                    if (processingPercent >= 100) {
                        clearInterval(processingInterval);
                        processingProgressBar.style.width = '100%';
                        processingProgressBar.setAttribute('aria-valuenow', 100);
                        processingProgressBar.textContent = '100%';
                        videoPlayer.src = response.output_file_url;
                        downloadLink.href = response.output_file_url;
                        videoContainer.style.display = 'block';
                    } else {
                        processingPercent += 10; // Simule o progresso do processamento
                        processingProgressBar.style.width = processingPercent + '%';
                        processingProgressBar.setAttribute('aria-valuenow', processingPercent);
                        processingProgressBar.textContent = Math.round(processingPercent) + '%';
                    }
                }, 1000);
            } else {
                alert('Error: ' + xhr.statusText);
            }
        });

        xhr.open('POST', form.action, true);
        xhr.send(formData);
    });
});
