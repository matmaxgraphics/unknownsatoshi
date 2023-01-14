    const articleButton = document.querySelector('.articleBtn');
    let articleItems = 3;
    articleButton.addEventListener('click', (e) => {
        const articleList = [...document.querySelectorAll('.blog-post__section #articleCard')];
        for (let i = articleItems; i < articleItems + 3; i++) {
            if (articleList[i]) {
                articleList[i].style.display = 'block';
            }
        }
        articleItems += 3;

        // Load more button will be hidden after list fully loaded
        if (articleItems >= articleList.length) {
            event.target.style.display = 'none';
        }
    })


    /*===========DIVIDER=============*/
    const newsButton = document.querySelector('.newsBtn');
    let newsItems = 3;
    newsButton.addEventListener('click', (e) => {
        const newsList = [...document.querySelectorAll('.blog-post__section #newsCard')];
        for (let i = newsItems; i < newsItems + 3; i++) {
            if (newsList[i]) {
                newsList[i].style.display = 'block';
            }
        }
        newsItems += 3;

        // Load more button will be hidden after list fully loaded
        if (newsItems >= newsList.length) {
            event.target.style.display = 'none';
        }
    })

/*===========DIVIDER=============*/
const storyButton = document.querySelector('.storyBtn');
let storyItems = 3;
storyButton.addEventListener('click', (e) => {
    const storyList = [...document.querySelectorAll('.blog-post__section #storyCard')];
    for (let i = storyItems; i < storyItems + 3; i++) {
        if (storyList[i]) {
            storyList[i].style.display = 'block';
        }
    }
    storyItems += 3;

    // Load more button will be hidden after list fully loaded
    if (storyItems >= storyList.length) {
        event.target.style.display = 'none';
    }
})

