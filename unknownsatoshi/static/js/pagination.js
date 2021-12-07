// $(".articleCard").slice(0, 3).show()
// 	$(".articlePageBtn").on("click", function(){
// 		$(".articleCard:hidden").slice(0, 3).slideDown()
// 		if($(".articleCard:hidden").length == 0){
// 			$(".articlePageBtn").fadeOut('slow')
// 		}
// })

// $(".newsCard").slice(0, 3).show()
// $(".newsPageBtn").on("click", function(){
//     $(".newsCard:hidden").slice(0, 3).slideDown()
//     if($(".newsCard:hidden").length == 0){
//         $(".newsPageBtn").fadeOut('slow')
//     }
// })

// $(".storyCard").slice(0, 3).show()
// $(".storyPageBtn").on("click", function(){
//     $(".storyCard:hidden").slice(0, 3).slideDown()
//     if($(".storyCard:hidden").length == 0){
//         $(".storyPageBtn").fadeOut('slow')
//     }
// })

/*==PAGINATION SCRIPT FOR COURSE PAGE==*/
$(".course-container__item").slice(0, 3).show()
    $(".coursePage").on("click", function(){
        $(".course-container__item:hidden").slice(0, 3).slideDown()
        if($(".course-container__item:hidden").length == 0){
            $(".coursePage").fadeOut('slow')
        }
})