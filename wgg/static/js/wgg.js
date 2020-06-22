// Runs once on page load to do initial populate of word board
$.getJSON($SCRIPT_ROOT + '/_scramble_word', {}, function(data) {
    $("#result").html(data.result);
});

// Runs once on page load to do initial populate of data stats
$.getJSON($SCRIPT_ROOT + '/_process_guess', {
    initial_set: 'Truey',
}, function(data) {
    $("#stats").html(data.stats);
});

// When the user wants the answer, this scripts adds a failure and resets
$(function() {
  $('a#calculate').bind('click', function() {
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
        initial_set: 'False',
      }, function(data) {
      $("#stats").html(data.stats);
    });
    return false;
  });
  $('#guessSubmit').bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/_check_word_refresh', {}, function(data) {
      $("#result").html(data.result);
    });
    return false;
  });
});
