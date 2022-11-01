$(document).ready(function() {  
    var s_round = '.s_round';  
    $(s_round).hover(function() {  
     $('.b_round').toggleClass('b_round_hover');  
     return false;  
    });  
    $(s_round).click(function() {  
     $('.flip_box').toggleClass('flipped');  
     $(this).addClass('s_round_click');  
     $('.s_arrow').toggleClass('s_arrow_rotate');  
     $('.b_round').toggleClass('b_round_back_hover');  
     return false;  
    });  
    $(s_round).on('transitionend', function() {  
     $(this).removeClass('s_round_click');  
     $(this).addClass('s_round_back');  
     return false;  
    });  
   });