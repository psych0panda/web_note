tinymce.init({
  selector: 'textarea',
  setup: function (editor) {
        editor.on('change', function () {
            editor.save();
        });
        },
  height: 500,
  menubar: 'tools',
  plugins: [
    'advlist autolink lists link image charmap print preview anchor textcolor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime media table contextmenu paste code help wordcount',
    'codesample',
  ],
  toolbar: 'insert | undo redo | codesample  |  formatselect | bold italic backcolor  | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help',
    codesample_languages: [
        {text: 'Python', value: 'python'},
        {text: 'HTML/XML', value: 'markup'},
        {text: 'JavaScript', value: 'javascript'},
        {text: 'CSS', value: 'css'},
        {text: 'Http', value: 'http'},
        {text: 'Django/Jinja2', value: 'django/jinja2'},
        {text: 'nginx', value: 'nginx'},
        {text: 'C', value: 'c'},
        {text: 'SQL', value: 'sql'},
        {text: 'Git', value: 'git'}
    ],
  content_css: [
    '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tinymce.com/css/codepen.min.css'],

});
