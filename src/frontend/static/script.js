const TIME_BETWEEN_SAME_SIGNS = 2000; // time in ms
const TIME_BETWEEN_SENDING_IMAGE = 200; // time in ms
const play_camera_btn = document.querySelector("#start-camera");
const stop_camera_btn = document.querySelector("#stop-camera");
const video = document.querySelector("#video");
const canvas = document.querySelector("#canvas");
const checkboxes = [...document.querySelectorAll(".check-item__checkbox")];
const signs_to_notification = {};
const last_notifications = {};
const signs_names_mapping = {};
let socket, intervalId;

checkboxes.forEach(checkbox => {
    const sign_id = checkbox.dataset.sign_id;
    signs_to_notification[sign_id] = undefined;
    signs_names_mapping[sign_id] = checkbox.parentNode.querySelector("label").innerHTML;
    checkbox.addEventListener("change", (_) => {
        signs_to_notification[sign_id] = checkbox.checked;
    })
})
function notify(signIdList){
    const currentTime = new Date().getTime();
    signIdList.forEach(sign_id => {
        if (last_notifications[sign_id] === undefined){
            speak(signs_names_mapping[sign_id])
        } else if (currentTime > last_notifications[sign_id] + TIME_BETWEEN_SAME_SIGNS){
            speak(signs_names_mapping[sign_id])
        }
        last_notifications[sign_id] = currentTime;
    })
}
function speak(text){
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 2;
    window.speechSynthesis.speak(utterance);
}

play_camera_btn.addEventListener('click', async function() {
    video.srcObject = null;
    video.srcObject = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    socket = new WebSocket(`ws://${location.host}/ws`);
    socket.onopen = function (){
        intervalId = setInterval(() => {
            if (socket) {
                canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
                let image_data_url = canvas.toDataURL('image/jpeg');
                socket.send(image_data_url);
            }
        }, TIME_BETWEEN_SENDING_IMAGE)
    }
    socket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        let notifications = []
        data.items.forEach(sign_id => {
            if (signs_to_notification.hasOwnProperty(sign_id)){
                notifications.push(sign_id)
            }
        })
        notify(notifications)
    };
});

stop_camera_btn.addEventListener('click', async function() {
    if (socket){
        clearInterval(intervalId);
        socket.close();
        video.srcObject = null;
    }
});