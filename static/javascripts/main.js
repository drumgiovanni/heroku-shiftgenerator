$(function(){
  let workersobj = {}
  $('#trigger').click(function(){
    $('.main-wrapper').animate({'height':'400px'}, 1500);
    $('#readme').fadeOut(1500);
    $('.workers-info').delay(500).show(2500);
    $(this).delay(500).fadeOut('slow');
  });

$('#register').click(function(){
  let workersinfo = {}
  let name = ""
  let type = ""
  let dayoff = ""
  name = $('#worker-name').val();
  $('#worker-name').val('');

  if ($('input[name=worker-type]:checked')) {
    console.log($('input[name=worker-type]:checked').val())
    type = $('input[name=worker-type]:checked').val();
    $('input[name=worker-type]:checked').prop('checked', false);
  }

  dayoff = $('#worker-dayoff').val();

  $('#worker-dayoff').val('')
  $('.show-worker').show();
  $('#person-list').append(`<ul> <li>名前：${name}</li> </ul>`);
  $('#person-list').append(`<p>    属性：${type}</p>`);
  $('#person-list').append(`<p>    休み希望：${dayoff}</p>`);
  $('#add-worker').css('display','block')
  $('#hidden-inputs').append(`<input type="text" name="worker-name" value="${name}" size="20"/>`);
  $('#hidden-inputs').append(`<input type="text" name="worker-type" value="${type}" />`);
  $('#hidden-inputs').append(`<input type="text" name="worker-dayoff" value="${dayoff}" size="20"/>`);
  });

});
