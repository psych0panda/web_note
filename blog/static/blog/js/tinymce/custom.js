tinymce.init({
  selector: 'textarea',
  setup: function (editor) {
        editor.on('change', function () {
            editor.save();
        });
        },
  height: 500,
  plugins: [
    'advlist autolink lists link image charmap print preview anchor textcolor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime media table contextmenu paste code help wordcount',
    'codesample code',
  ],
  codesample_languages: [
        {text: 'HTML/XML', value: 'markup'},
        {text: 'CSS', value: 'css'},
        {text: 'C', value: 'c'},
        {text: 'JavaScript', value: 'javascript'},
        {text: 'Git', value: 'git'},
        {text: 'Json', value: 'json'},
        {text: 'SQL', value: 'sql'},
        {text: 'Python', value: 'python'},
    ],
  toolbar: 'insert | undo redo | codesample code  |  formatselect | bold italic backcolor  | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help',
  content_css: [
    '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tinymce.com/css/codepen.min.css'],

});
