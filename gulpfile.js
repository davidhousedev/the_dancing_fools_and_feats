const gulp = require('gulp'), // gulp package
    sass = require('gulp-sass'), // sass compiler
    cssmin = require('gulp-clean-css'), // minify css
    imageResize = require('gulp-image-resize'), // resize images
    path = require('path'), // node.js module that serve path
    rename = require("gulp-rename"), //rename module
    autoprefixer = require('gulp-autoprefixer'); //prefixes for cross-browser compatibility

var sassOptions = { //sass compiler options
        errLogToConsole: true,
        outputStyle: 'expanded'
    },
    rootPath = './'; //project root path

gulp.task('sass', function() {
    var src = path.join(rootPath, '**', 'static/', '**', 'scss');
    console.log(src);
    return gulp.src(path.join(src, '*.scss'), {base: '.'})
        .pipe(sass(sassOptions).on('error', sass.logError)) // sass to css compilation
        .pipe(autoprefixer()) //  prefixes for cross-browsers compatibility
        .pipe(cssmin()) // minimize css file size
        .pipe(rename(function (path) { // here is the place where rename of scss folder in source path to css and send it to destination path
            path.dirname = path.dirname.replace('/scss', '/css');
            path.extname = '.css';
        }))
        .pipe(gulp.dest('.')); //write compilation result
});


const img_sizes = {
    xs: 200,
    sm: 400,
    md: 800,
    lg: 1600,
    xlg: 2000
};

var imgResizeTasks = [];
for (var size in img_sizes) {
    if (!img_sizes.hasOwnProperty(size)) {
        continue
    }
    var taskName = 'resize_' + size;
    function createTask(taskName, img_size, width) {
        gulp.task(taskName, function() {
            var src = path.join(rootPath, './static', '**', 'img/src');
            return gulp.src(path.join(src, '*.jpg'), {base: '.'})
                .pipe(imageResize({
                    width: width,
                    crop: false
                }))
                .pipe(rename(function (path) {
                    path.dirname = path.dirname.replace('/src', '/dist/' + img_size);
                    path.extname = '.jpg';
                }))
                .pipe(gulp.dest('.'))
        });
    }
    createTask(taskName, size, img_sizes[size]);
    imgResizeTasks.push(taskName);
}


gulp.task('watch', function () { // watch for changes in all scss files
    var src = path.join(rootPath, '**', '*.scss');
    gulp.watch(src, ['sass']); //recompile all files on scss change
});

gulp.task('imgs', imgResizeTasks);
gulp.task('default', ['sass', 'imgs', 'watch']);
