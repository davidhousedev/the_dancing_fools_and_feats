const gulp = require('gulp'), // gulp package
    sass = require('gulp-sass'), // sass compiler
    cssmin = require('gulp-clean-css'), // minify css
    path = require('path'), // node.js module that serve path
    rename = require("gulp-rename"), //rename module
    autoprefixer = require('gulp-autoprefixer'); //prefixes for cross-browser compatibility

var sassOptions = { //sass compiler options
        errLogToConsole: true,
        outputStyle: 'expanded'
    },
    rootPath = './'; //project root path

gulp.task('sass', function() {
    var src = path.join(rootPath, './static/', '**', 'scss');
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

gulp.task('watch', function () { // watch for changes in all scss files
    var src = path.join(rootPath, '**', '*.scss');
    gulp.watch(src, ['sass']); //recompile all files on scss change
});

gulp.task('default', ['sass', 'watch']);
