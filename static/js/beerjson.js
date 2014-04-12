
 $(document).ready(function() {
          $("#id_beer").change(function () {
            var choice = jQuery(this).val();
            $.ajax({
              url:'/beer/json/',
              type:'GET',
              data : {'pk' : choice},
              success : function(response) {
              var fields = response[0].fields
              $("#id_og_actual").val(fields.og_estimated);
              $("#id_fg_actual").val(fields.fg_estimated);
              $("#id_srm_actual").val(fields.srm_estimated);
              $("#id_ibu_actual").val(fields.ibu_estimated);
              }
            });
          });
        })

