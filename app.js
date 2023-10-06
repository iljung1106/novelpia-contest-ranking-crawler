// 이 파일에는 주 로직이 포함됩니다.
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('show-data1').addEventListener('click', function() {
        parseAndDisplayData(data1);
    });

    document.getElementById('show-data2').addEventListener('click', function() {
        parseAndDisplayData(data2);
    });
});

function parseAndDisplayData(data) {
    const lines = data.trim().split('\n');
    const container = document.getElementById('data-container');
    container.innerHTML = "";
    
    let i = 0
    lines.forEach(line => {
        i++
        const [title, data1, data2, imageUrl] = line.split(',,');
        
        const div = document.createElement('div');
        const h2 = document.createElement('h2');
        const p1 = document.createElement('p');
        const img = document.createElement('img');
        const hr = document.createElement('hr');

        h2.textContent = i + "위 : " + title;
        p1.textContent = "조회수 : " + data1 + "   추천 : " + data2;
        img.src = imageUrl;

        
        div.appendChild(h2);
        div.appendChild(p1);
        div.appendChild(img);
        div.appendChild(hr)
        

        container.appendChild(div);
        if(i >= 100){
            return
        }
    });
}
