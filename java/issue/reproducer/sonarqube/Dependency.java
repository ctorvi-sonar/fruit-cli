package issue.reproducer.sonarqube;

import java.io.File;
import java.io.IOException;

public class Dependency {

    public static final String FILE_SEPARATOR = "/"; //$NON-NLS-1$
    public static final String ENTRY_SEPARATOR = "#"; //$NON-NLS-1$

    public static String ROOT = _pathConform("/root");

    protected static String TRUE_FS_ROOT;

    Connection conn = DriverManager.getConnection("jdbc:derby:memory:myDB;create=true", "login", ""); // Noncompliant

    static {
        try {
            TRUE_FS_ROOT = _pathConform(new File(ROOT).getCanonicalPath());
            // do something
        } catch (IOException ioe) {
            // do something
        }
    }

    public static String pathConform(String path) {

        return path == null ? null :
            mapDriveSpec(mapTrueFilesystemPath(_pathConform(path)));
    }

    private static String _pathConform(String path) {
        if( path == null ) {
            return null;
        }

        char target = '\\';
        char fileSeparator = File.separatorChar;

        String head = path;
        String tail = null;
        int z;
        if( 0 <= (z = path.indexOf(ENTRY_SEPARATOR)) ) {
            head = path.substring(0, z);
            tail = path.substring(z);
        }

        if ( ! (target == fileSeparator && head.indexOf(target) >= 0) ) {
            head = resolveRelativePathComponents(head);
            return tail == null ? head : head + tail;
        }

        // replace separators
        char[] buf = new char[head.length()];
        head.getChars(0, head.length(), buf, 0);

        // do something

        head = resolveRelativePathComponents(new String(buf));
        return tail == null ? head : head + tail;
    }

    protected static String mapTrueFilesystemPath(String path) {
        if(ROOT.startsWith(TRUE_FS_ROOT))
            return path;
        if(!path.startsWith(TRUE_FS_ROOT))
            return path;
        return catpath(ROOT, path.substring(TRUE_FS_ROOT.length()));
    }

    protected static String mapDriveSpec(String path) {
        // do something
        return path;
    }

    protected static String resolveRelativePathComponents(String path) {
        // do something
        return path;
    }

    public static String catpath(String pathHead, String pathTail) {
        String s =  pathHead + FILE_SEPARATOR + pathTail;
        // do something
        return s;
    }
}
