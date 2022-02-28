<script>
$(.operation).ready(function() {
   
    var e = $(this);
    var title = e.data('title').charAt(0).toUpperCase() + e.data('title').slice(1);
    var compte = e.data('value');
    $('.modal-title').html(title);

    if((e.data('title') == 'update')) {
        $("#update_profil #profil").attr('value', e.data('value'));
        $("update_profil #profil").attr('name', 'elementSelecte');
        $("#retrait_depot").show();
        $("#virement").hide();
    }
    )))

    $('#modalOperation').modal('show');

    )}};
$(document).ready(function(){
        $('input[type="radio"]').click(function(){
          var val = $(this).attr("value");
          var target = $("." + val);
          $(".msg").not(target).hide();
//           $(".msg").not(target).display()
          $(target).show();
        });
      });
    </script>
</script>


<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-Piv4xVNRyMGpqkS2by6br4gNJ7DXjqk09RmUpJ8jgGtD7zP9yug3goQfGII0yAns" crossorigin="anonymous"></script>
	
