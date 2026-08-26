document.addEventListener("DOMContentLoaded", function () {
  const menuItems = document.querySelectorAll('.menu-item');

  menuItems.forEach(menuItem => {
    menuItem.addEventListener('click', function (e) {
      e.preventDefault();

      // Скрываем другие активные подменю
      document.querySelectorAll('.submenu.active').forEach(submenu => {
        if (submenu !== this.nextElementSibling) {
          submenu.classList.remove('active');
        }
      });

      // Переключаем текущее подменю
      const submenu = this.nextElementSibling;
      if (submenu && submenu.classList.contains('submenu')) {
        submenu.classList.toggle('active');
      }
    });
  });

  // Закрываем все подменю при клике вне сайдбара
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.sidebar')) {
      document.querySelectorAll('.submenu.active').forEach(submenu => {
        submenu.classList.remove('active');
      });
    }
  });
});
