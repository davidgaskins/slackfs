import os, sys, errno
from fuse import FUSE, FuseOSError, Operations
from SlackCommand import SlackCommand, SlackFile

debug = True
#based upon IssueFS, licensed based upon MIT

class SlackFS(Operations):
    def __init__(self):
        self.channels = SlackCommand("channels.list").get_url({}).get("channels")

    def _contents(self, path):
        # Return contents of a given path
        # For now, return the issue title and body concatenated
        if debug: print('_contents path: {}'.format(path))

        #parse the file name and type
        try:
            slack_stream = SlackFile(path)
        except:
            return False

        if debug: print('_contents stream: {}'.format(path))
        slack_stream
        # Get Github issue
        gh = login(self.username, self.password)
        issue = gh.issue(self.username, self.repo, issue)

        # Concatanate issue title and body and return as file content
        file_contents =  slack_stream._contents()
        if debug: print('_contents file_contents: {}'.format(file_contents))
        return file_contents

    # Filesystem methods
    # ==================

    def access(self, path, mode):
        if debug: print('access mode: {}, path: {}'.format(mode, path))
        # Mock
        if False:
            raise FuseOSError(errno.EACCES)

    def chmod(self, path, mode):
        if debug: print('chmod mode: {}, path: {}'.format(mode, path))
        # Mock
        return True

    def chown(self, path, uid, gid):
        if debug: print('chown uid: {}, gid: {}, path: {}'.format(uid, gid, path))
        # Mock
        return True

    def getattr(self, path, fh=None):
        if debug: print('getattr path: {}'.format(path))

        ignore_paths = ['/._.', '.gitignore']

        # If path is a directory
        if path.endswith('/'):
            s = {'st_ctime': 1450647916.0, 'st_mtime': 1450647886.0, 'st_nlink': 19, 'st_mode': 16877, 'st_size': 0, 'st_gid': 20, 'st_uid': 501, 'st_atime': 1455426628.0}
        # Else if path is a hidden file
        elif ('/.' in path):
            s = {'st_ctime': 1450647916.0, 'st_mtime': 1450647886.0, 'st_nlink': 19, 'st_mode': 33188, 'st_size': 0, 'st_gid': 20, 'st_uid': 501, 'st_atime': 1455426628.0}
        # Else if path is anything else, assume it's an issue entry
        else:
            path_content = self._contents(path)
            s = {'st_ctime': 1450647916.0, 'st_mtime': 1450647886.0, 'st_nlink': 19, 'st_mode': 33188, 'st_size': len(path_content), 'st_gid': 20, 'st_uid': 501, 'st_atime': 1455426628.0}
        return s

    def readdir(self, path, fh):
        if debug: print('readdir path: {}'.format(path))

        # If root of device...
        if path == '/':
            # Add . and .. entries to children array
            children = ['.', '..']

            # Get List of Channels
            self.channels = SlackCommand("channels.list").get_url({}).get("channels")
            supported_file_types = ["chat", "pins", "files", "info"]
            # Add the channel name to the
            for channel in self.channels:
                for file_type in supported_file_types:
                    file_name = '{}_{}.{}'.format(channel.get("name"), channel.get("id"),file_type)
                    children.append(file_name)

            # Return a generator object for each entry in children
            for entry in children:
                if debug: print(entry)
                yield entry

    def readlink(self, path):
        if debug: print('readlink path: {}'.format(path))
        # Mock
        return path

    def mknod(self, path, mode, dev):
        if debug: print('mknod path: {}'.format(path))
        # Mock
        return

    def rmdir(self, path):
        if debug: print('rmdir path: {}'.format(path))
        # Mock
        return path

    def mkdir(self, path, mode):
        if debug: print('mkdir path: {}'.format(path))
        # Mock
        return

    def statfs(self, path):
        if debug: print('statfs path: {}'.format(path))
        # Mocked up statfs return values for now
        # Mostly nonsensical but functional
        return {'f_bsize': 1048576, 'f_bavail': 0, 'f_favail': 7745916, 'f_files': 3, 'f_frsize': 4096, 'f_blocks': 29321728, 'f_ffree': 7745916, 'f_bfree': 0, 'f_namemax': 255, 'f_flag': 0}

    def unlink(self, path):
        if debug: print('unlink path: {}'.format(path))
        # Mock
        return

    def symlink(self, name, target):
        if debug: print('symlink name: {}, target: {}'.format(name, target))
        # Mock
        return

    def rename(self, old, new):
        if debug: print('rename old: {}, new: {}'.format(old, new))
        # Mock
        return

    def link(self, target, name):
        if debug: print('link name: {}, target: {}'.format(name, target))
        # Mock
        return

    def utimens(self, path, times=None):
        if debug: print('utimens path: {}'.format(path))
        # Mock
        return

    # File methods
    # ============

    def open(self, path, flags):
        if debug: print('open path: {}'.format(path))
        # Mock
        return True

    def create(self, path, mode, fi=None):
        if debug: print('create path: {}, mode: {}'.format(path, mode))
        # Mock
        return

    def read(self, path, length, offset, fh):
        if debug: print('read path: {} - {}:{}'.format(path, length, offset))
        # Retrieve contents, apply read offsets, and return
        # Added str() explicitly to return a byte array which read() expects
        return str(self._contents(path)[offset:offset+length])

    def write(self, path, buf, offset, fh):
        if debug: print('write path: {}, offset: {}'.format(path, offset))
        # Mock
        return True

    def truncate(self, path, length, fh=None):
        if debug: print('truncate path: {}, length: {}'.format(path, length))
        # Mock
        return True

    def flush(self, path, fh):
        if debug: print('flush path: {}'.format(path))
        # Mock
        return True

    def release(self, path, fh):
        if debug: print('release path: {}'.format(path))
        # Mock
        return True

    def fsync(self, path, fdatasync, fh):
        if debug: print('fsync path: {}'.format(path))
        # Mock
        return True
def main():
    # Create new FUSE filesystem at designated mountpoint using IssueFS
    FUSE(SlackFS(), "/home/vagrant/tmp", nothreads=True, foreground=True)


if __name__ == '__main__':
    main()
