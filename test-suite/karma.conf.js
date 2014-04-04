// Karma configuration
// Generated on Wed Jan 29 2014 15:32:16 GMT+0100 (CET)


// SID: get WORKSPACE_URL configuration from one single file to customize
var w = require ('./workspace.info.js'),
	t = require ('./lib/test_hlp.js');

module.exports = function(config) {
	config.set({
		// list of files or patterns to load in the browser, from current directory
		files: [
			{pattern: 'tests/**/*.js', included: true}
		],
		// list of files to exclude
		exclude: [
		],
		// Start these browsers, currently available:
		// - Firefox	; Safari	(only Mac; run `npm install karma-safari-launcher` first)
		// - Chrome		; ChromeCanary ; Opera (run `npm install karma-opera-launcher` first)
		// - PhantomJS	; IE		(only Windows; run `npm install karma-ie-launcher` first)
		browsers: w.BROWSERS,
		// frameworks to use. SID: choosen mocha, added karma-e2e-dsl (end-to-end testing)
		frameworks: ['mocha', 'karma-e2e-dsl'],
		// SID: Karma will start and run somewhere else than '/', to allow proxying '/'
		urlRoot: '/karma/',
		// SID: directive added on karma-e2e-dsl purpose. Map of path-proxy pairs.
		proxies: {
			'/': w.WORKSPACE_URL
		},
		client: {
			mocha: {
				ui: 'tdd'
			},
			w: w, // SID: exports the variable in the test execution browser window
			// SID: we can't pass living functions to testing (mocha) browser environment
			// so we convert them to string, and send also a string body of a reviving function
			// closures are lost in the process, that's ok.
			t: JSON.stringify (t, function (k, v) { return typeof v === 'function' ? v.toString () : v }),
			r: t.reviveFunc
		},
		// test results reporter to use : 'dots', 'progress', 'junit', 'growl', 'coverage'
		reporters: ['progress'],
		// web server port
		port: 9876,
		// enable / disable colors in the output (reporters and logs)
		colors: true,
		// level of logging : config.LOG_DISABLE || _ERROR || _WARN || _INFO || _DEBUG
		logLevel: config.LOG_INFO,
		// If browser does not capture in given timeout [ms], kill it
		captureTimeout: 9999,
		// enable / disable watching file and executing tests whenever any file changes
		autoWatch: false,
		// Continuous Integration mode : if true, it capture browsers, run tests and exit
		singleRun: true,
	});
};