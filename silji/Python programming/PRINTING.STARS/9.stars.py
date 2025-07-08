#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
rows = 5

for i in range(rows):
            # Print leading spaces
     print("  " * (rows - i - 1), end="")

            # Print stars with space
     print("* " * (2 * i + 1))