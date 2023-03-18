
var view =  document.getElementById('views');
console.log(view);
function countVisitor(){
    let count = localStorage.getItem('visitorCount');
    if (count === null) {
        count = 1;
    }else {
        count = parseInt(count)+1;
    }
    localStorage.setItem('visitorCount',count);
    view.innerHTML= count;
    return count;
}



