package issue.reproducer.sonarqube;

import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.File;

public class Reproducer extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) {
        String filepath = request.getParameter("filepath");

        filepath = Dependency.pathConform(filepath);

        String filename = filepath;

        File f = new File(filename);

        if (f.exists() && f.isFile()) { // this line reports the issue.
            // do something
        }
    }
}