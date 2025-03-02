require("dotenv").config(); // Load environment variables
const express = require("express");
const app = express();
const path = require("path");
const passport = require("passport");
const session = require("express-session");
const mongoose = require("mongoose");
const User = require("./models/User");  // Import User model
const LocalStrategy = require("passport-local").Strategy;
const GoogleStrategy = require("passport-google-oauth20").Strategy;
const bodyParser = require("body-parser");
const multer = require("multer");
const { PythonShell } = require("python-shell");
const fs = require("fs");

// Connect to MongoDB
mongoose.connect(process.env.DB_LINK, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => console.log("MongoDB Connected"))
    .catch(err => console.error(err));

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false
}));

app.use(passport.initialize());
app.use(passport.session());

// Configure Passport Local Strategy
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

passport.use(new GoogleStrategy({
    clientID: process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    callbackURL: process.env.GOOGLE_CALLBACK_URL
}, (accessToken, refreshToken, profile, done) => {
    return done(null, profile);
}));

// Set EJS as the template engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.static(path.join(__dirname, "public")));

// Routes
app.get("/", (req, res) => res.render("home"));
app.get("/about", (req, res) => res.render("about"));
app.get("/attacks", (req, res) => res.render("attacks"));
app.get("/features", (req, res) => res.render("features"));
app.get("/login", (req, res) => res.render("login"));
app.get("/register", (req, res) => res.render("register"));

// Google Authentication Routes
app.get("/auth/google",
    passport.authenticate("google", { scope: ["profile", "email"] })
);

app.get("/auth/google/callback",
    passport.authenticate("google", { failureRedirect: "/login" }),
    (req, res) => res.redirect("/submit")
);

app.get("/submit", (req, res) => {
    if (req.isAuthenticated()) {
        res.render("submit");
    } else {
        res.redirect("/login");
    }
});

// Logout Route
app.get("/logout", function (req, res) {
    req.logout(() => {
        res.redirect("/");
    });

    if (submitted_csv_file !== "") {
        let filePath = path.join(__dirname, "Uploaded_files", submitted_csv_file);
        fs.unlink(filePath, (err) => {
            if (err) {
                console.log(err);
            } else {
                console.log("File deleted");
            }
            submitted_csv_file = "";
        });
    }
});

// Register Route
app.post("/register", (req, res) => {
    User.register(new User({ username: req.body.username }), req.body.password, (err, user) => {
        if (err) {
            console.log(err);
            return res.redirect("/register");
        }
        passport.authenticate("local")(req, res, () => res.redirect("/submit"));
    });
});

// Login Route
app.post("/login", passport.authenticate("local", {
    successRedirect: "/submit",
    failureRedirect: "/login"
}));

// File Upload Configuration
let submitted_csv_file = "";
const storage = multer.diskStorage({
    destination: function (req, file, callback) {
        callback(null, "./Uploaded_files");
    },
    filename: function (req, file, callback) {
        submitted_csv_file = file.originalname;
        console.log("Uploaded File: ", submitted_csv_file);
        callback(null, file.originalname);
    }
});

const upload = multer({ storage: storage }).single("myfile");

// File Upload and Prediction Route
app.post("/uploadjavatpoint", function (req, res) {
    upload(req, res, function (err) {
        if (err) {
            return res.status(500).json({ error: "Error uploading file." });
        }
        console.log("File uploaded successfully!");

        const submitted_model = req.body.selected_model;
        console.log("Selected Model:", submitted_model);
        console.log("Submitted CSV File:", submitted_csv_file);

        let predicted_file = submitted_csv_file.replace(".csv", "_predicted.csv");
        let predicted_file_path = path.join(__dirname, "Uploaded_files", predicted_file);

        let options = {
            args: [submitted_model, submitted_csv_file, predicted_file_path] // Ensure the Python script knows where to save the file
        };

        PythonShell.run("nids_updated_csv.py", options, (err, response) => {
            if (err) {
                console.error("Error running Python script:", err);
                return res.status(500).json({ error: "Error processing file." });
            }
            console.log("Prediction completed! File ready for download:", predicted_file_path);

            res.json({ 
                message: "Prediction complete!", 
                download_url: `/download-file?filename=${predicted_file}`
            });
        });
    });
});

// Download Prediction Result Route (Fixed)

app.get("/download-file", (req, res) => {
    if (!submitted_csv_file) {
        return res.status(400).json({ error: "No file available for download." });
    }

    let filePath = path.join(__dirname, "Uploaded_files", submitted_csv_file);

    console.log("Downloading file:", filePath);
    res.download(filePath, submitted_csv_file, (err) => {
        if (err) {
            console.error("Download error:", err);
            res.status(500).json({ error: "Error downloading file." });
        }
    });
});



// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
