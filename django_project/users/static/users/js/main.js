$(document).ready(function(){
  var loadForm = function () { 
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal .modal-content").html("");
        $("#modal").modal("show");
      },
      success: function (data) {
        $("#modal .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#product-table tbody").html(data.html_product_list);
          $("#modal").modal("hide");<font></font>
        }
        else {
          $("#modal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };
  /* Binding */<font style="vertical-align: inherit;"/>
  $(".js-create-product").click(loadForm);<font style="vertical-align: inherit;"/>
  $("#modal").on("submit", ".js-product-create-form", saveForm);
  <font style="vertical-align: inherit;"/>
  // Mettre à jour le produit</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
  $("#product-table").on("click", ".js-update-product", loadForm);<font style="vertical-align: inherit;"/>
  $("#modal").on("submit", ".js-product-update-form", saveForm);

 <font style="vertical-align: inherit;"/>
});