
 $(document).ready(function() {
          $("#id_beer").change(function () {
            var choice = jQuery(this).val();
            $.ajax({
              url:'/beer/json/',
              type:'GET',
              data : {'pk' : choice},
              success : function(response) {
              var fields = response[0].fields
              $("#id_ogAct").val(fields.ogEst);
              $("#id_fgAct").val(fields.fgEst);
              $("#id_srmAct").val(fields.srmEst);
              $("#id_ibuAct").val(fields.ibuEst);
              }
            });
          });
        })

