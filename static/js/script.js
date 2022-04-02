let title_article = document.getElementById('title_article').innerText;

function visibility() {
  let visible_links = document.getElementById('indiv_links').style.display = "block";
  let aritcle_form = document.getElementById('article_form').style.display= 'none';


}
function wrapper(func) {
  if (title_article === "") {
    console.log('empty title');
  }
  else {
    return func();
  }
}
wrapper(visibility)