import json

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs_preorder(root):
            if not root:
                result.append(None)
                return

            result.append(root.val)
            dfs_preorder(root.left)
            dfs_preorder(root.right)

        dfs_preorder(root)

        return json.dumps(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = json.loads(data)

        index = 0

        def build_tree():
            nonlocal index

            if arr[index] is None:
                index += 1
                return None

            root = TreeNode(arr[index])
            index += 1

            root.left = build_tree()
            root.right = build_tree()

            return root

        return build_tree()