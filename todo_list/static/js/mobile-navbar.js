
/**
 * Event listener for the DOMContentLoaded event.
 * This event is fired when the initial HTML document has been completely loaded and parsed,
 * without waiting for stylesheets, images, and subframes to finish loading. 
*/

document.addEventListener('DOMContentLoaded', () => {
    const hamburgerMenu = document.querySelector("#hamburger-menu");
    const menuBars = document.querySelectorAll(".menu-bar");
    const overlay = document.querySelector("#overlay");
    const nav1 = document.querySelector("#nav-1");
    const nav2 = document.querySelector("#nav-2");
    const nav3 = document.querySelector("#nav-3");
    const nav4 = document.querySelector("#nav-4");
    const nav5 = document.querySelector("#nav-5");
    const nav6 = document.querySelector("#nav-6");
    const nav7 = document.querySelector("#nav-7");
    const navItems = [nav1, nav2, nav3, nav4, nav5, nav6, nav7];

    const aiLink = document.querySelector("#ai-link");
    
    // Dark menu
    document.addEventListener("scroll", () => {
        if (window.scrollY > 1) {
            menuBars.forEach(bar => {
                bar.classList.add("menu-bar-dark");
            })
        } else {
            menuBars.forEach(bar => {
                bar.classList.remove("menu-bar-dark");
            })
        }
    });

    // Control Navigation Animation
    function navAnimation(val1, val2) {
        navItems.forEach((nav, i) => {
            if (nav) {
                nav.classList.replace(`slide-${val1}-${i + 1}`, `slide-${val2}-${i + 1}`);
            }
        });
    }

    function toggleNav() {
        // Toggle: Hamburger Open/Close
        hamburgerMenu.classList.toggle("active");

        //   Toggle: Menu Active
        overlay.classList.toggle("overlay-active");

        if (overlay.classList.contains("overlay-active")) {
            // Animate In - Overlay
            overlay.classList.replace("overlay-slide-left", "overlay-slide-right");
            
            // Animate In - Nav Items
            navAnimation("out", "in");

            // Overlap AI Link
            if (aiLink) {
                aiLink.classList.add("ai-link-overlaped");
            } else {
                console.warn("AI Link is on the other pages");
            }
            
        } else {
            // Animate Out - Overlay
            overlay.classList.replace("overlay-slide-right", "overlay-slide-left");

            // Animate Out - Nav Items
            navAnimation("in", "out");

            // Unoverlap AI Link 
            if (aiLink) {
                aiLink.classList.remove("ai-link-overlaped");
            } else {
                console.warn("AI Link is on the other pages ");
            }
           
        }
    }

    // Events Listeners
    hamburgerMenu.addEventListener("click", toggleNav);

    navItems.forEach((nav) => {
        if (nav) {
            nav.addEventListener("click", toggleNav);
        }
    });

    // Close the menu when user change window orientation
    function closeOverlayMenu(windowWidth) {
        if (windowWidth.matches) { // If media query matches
            hamburgerMenu.classList.remove("active");
            overlay.classList.remove("overlay-active");
            overlay.classList.replace("overlay-slide-right", "overlay-slide-left");
            navAnimation("in", "out");
        }
        
      }
      
      // Create a MediaQueryList object
      var windowWidth = window.matchMedia("(min-width: 535px)")
      // Call listener function at run time
      closeOverlayMenu(windowWidth);
      
      // Attach listener function on state changes
      windowWidth.addEventListener("change", function() {
        closeOverlayMenu(windowWidth);
      });

});