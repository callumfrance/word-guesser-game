// Runs once on page load to do initial populate of word board
$.getJSON($SCRIPT_ROOT + '/_word_page_initial', {}, function(data) {
        $("#result").html(data.result),
        $("#stats").html(data.stats);
});

// When the user wants the answer, this scripts adds a failure and resets
$(function() {
  $('#calculate').bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/_give_up_answer', {}, function(data) {
      $("#result").html(data.result),
      $("#stats").html(data.stats);
    });
    return false;
  });
});

// The user submits a guess and this processes it
$(function() {
  $('#guessSubmit').bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/_process_guess', {
        guess: $('input[name="guess"]').val(),
      }, function(data) {
      $("#result").html(data.result),
      $("#stats").html(data.stats);
    });
    return false;
  });
});
