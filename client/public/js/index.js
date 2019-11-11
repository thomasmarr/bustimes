
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);

    var sideLinks = document.querySelectorAll('.sidenavlink');

    sideLinks.forEach(sideLink => {
      sideLink.addEventListener('click', () => {
        instances.forEach(instance=>instance.close())
      })
    })
  });
